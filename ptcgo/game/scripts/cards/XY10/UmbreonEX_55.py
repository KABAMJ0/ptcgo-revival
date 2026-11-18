from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="64ad5acf-2836-538e-81b2-4ad3fd349a32",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonEX.Name",
    display_name="Umbreon-EX",
    searchable_by=["Umbreon-EX", "Basic", "EX", "UmbreonEX"],
    subtypes=["Basic", "EX"],
    collector_number=55,
    set_code="XY10",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=197,
    abilities=[
        Attack(
            title="Veil of Darkness",
            game_text="Discard as many cards as you like from your hand. Then, draw that many cards.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Endgame",
            game_text="If your opponent's Mega Evolution Pok\u00e9mon is Knocked Out by damage from this attack, take 2 more Prize cards.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)