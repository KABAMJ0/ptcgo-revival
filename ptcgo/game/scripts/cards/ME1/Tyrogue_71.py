from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="6635d381-0143-57d1-afac-5ffbb6479534",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrogue.Name",
    display_name="Tyrogue",
    searchable_by=["Tyrogue", "Basic", "Tyrogue"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=236,
    abilities=[
        Attack(
            title="Pow-Pow Punching",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={},
            damage=10,
            damage_operator="+",
            effect=flip_damage(until_tails=True, per_heads=30, base=10),
        ),
    ],
)