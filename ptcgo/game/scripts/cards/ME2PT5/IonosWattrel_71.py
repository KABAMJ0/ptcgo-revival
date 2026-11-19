from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e507e039-ac28-56a4-88b9-45f908588dc2",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosWattrel.Name",
    display_name="Iono's Wattrel",
    searchable_by=["Iono's Wattrel", "Basic", "IonosWattrel"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=940,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)