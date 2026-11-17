from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="15820eef-0e7d-5007-ba62-3a5926056e82",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiosGX.Name",
    display_name="Latios-GX",
    searchable_by=["Latios-GX", "Basic", "GX", "LatiosGX"],
    subtypes=["Basic", "GX"],
    collector_number=78,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=381,
    abilities=[
        Ability(
            title="Power Bind",
            game_text="If you have 4 or fewer Pok\u00e9mon in play, this Pok\u00e9mon can't attack.",
            effect=unimplemented,
        ),
        Attack(
            title="Tag Purge",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from TAG TEAM Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
        Attack(
            title="Clear Vision-GX",
            game_text="For the rest of this game, your opponent can't use any GX attacks. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)