from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2a5dc0a1-a784-540f-8252-66ef92eac375",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegirockEX.Name",
    display_name="Regirock-EX",
    searchable_by=["Regirock-EX", "Basic", "EX", "RegirockEX"],
    subtypes=["Basic", "EX"],
    collector_number=43,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Ability(
            title="Regi Power",
            game_text="The attacks of your Fighting Pok\u00e9mon (excluding Regirock-EX) do 10 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Bedrock Press",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)