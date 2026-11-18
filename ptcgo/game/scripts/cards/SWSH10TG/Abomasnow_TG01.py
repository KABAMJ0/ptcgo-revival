from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a03fd19a-0e2d-5264-bac7-6b65fcc8c577",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name",
    display_name="Abomasnow",
    searchable_by=["Abomasnow", "Stage 1", "Single Strike", "Abomasnow"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=1,
    set_code="SWSH10TG",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=460,
    abilities=[
        Ability(
            title="Toughness Boost",
            game_text="Your Single Strike Pok\u00e9mon in play, except any Abomasnow, get +50 HP. You can't apply more than 1 Toughness Boost Ability at a time.",
            effect=unimplemented,
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)