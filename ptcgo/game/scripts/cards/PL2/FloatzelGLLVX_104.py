from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e79af2ec-1cc6-5923-966e-a12b01f1328c",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FloatzelGLLVX.Name",
    display_name="Floatzel GL LV.X",
    searchable_by=["Floatzel GL LV.X", "Level-Up", "SP", "FloatzelGLLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=104,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.FloatzelGL.Name",
    family_id=419,
    abilities=[
        Ability(
            title="Water Rescue",
            game_text="Whenever any of your Water Pok\u00e9mon (excluding any Floatzel GL) is Knocked Out by damage from your opponent's attack, you may put that Pok\u00e9mon and all cards that were attached to it from your discard pile into your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Cyclone",
            game_text="Choose as many Energy cards from your hand as you like and show them to your opponent. This attack does 20 damage times the number of Energy cards you chose. Put those Energy cards on top of your deck. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)