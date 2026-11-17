from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3ce103a4-5ab6-5ef6-b8b3-1b7892796365",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaGLVX.Name",
    display_name="Palkia G LV.X",
    searchable_by=["Palkia G LV.X", "Level-Up", "SP", "PalkiaGLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=125,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaG.Name",
    family_id=484,
    abilities=[
        Ability(
            title="Lost Cyclone",
            game_text="Once during your turn (before your attack), you may use this power. Any player who has 4 or more Benched Pok\u00e9mon chooses 3 of his or her Benched Pok\u00e9mon. Put the other Benched Pok\u00e9mon and all cards attached to them in the Lost Zone. (You choose your Pok\u00e9mon first.) This power can't be used it Palkia G is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Shot",
            game_text="Discard 2 Energy attached to Palkia G. Choose 1 of your opponent's Pok\u00e9mon. This attack does 80 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)