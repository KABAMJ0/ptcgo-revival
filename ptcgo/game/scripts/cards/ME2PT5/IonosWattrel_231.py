from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7586e209-0498-5db6-a432-7965ff869426",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosWattrel.Name",
    display_name="Iono's Wattrel",
    searchable_by=["Iono's Wattrel", "Basic", "IonosWattrel"],
    subtypes=["Basic"],
    collector_number=231,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
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