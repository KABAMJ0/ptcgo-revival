from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6bde0164-94ac-50dc-bb94-d5f3346a3579",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaCharizardXex.Name",
    display_name="Mega Charizard X ex",
    searchable_by=["Mega Charizard X ex", "Stage 2", "MEGA", "ex", "MegaCharizardXex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=130,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=360,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Inferno X",
            game_text="Discard any amount of Fire Energy from among your Pok\u00e9mon, and this attack does 90 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2},
            damage=90,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)