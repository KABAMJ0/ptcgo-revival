from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5d359566-67bd-53f9-ad30-0d51121fec68",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    display_name="Ferroseed",
    searchable_by=["Ferroseed", "Basic", "Ferroseed"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=597,
    abilities=[
        Attack(
            title="Continuous Tumble",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=20),
        ),
    ],
)