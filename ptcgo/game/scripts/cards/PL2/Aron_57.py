from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3e5b1d25-6992-5715-82fe-4c36dc2f5c08",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    display_name="Aron",
    searchable_by=["Aron", "Basic", "Aron"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=304,
    abilities=[
        Attack(
            title="Iron Head",
            game_text="Flip a coin until you get tails. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(per_heads=10, until_tails=True),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)