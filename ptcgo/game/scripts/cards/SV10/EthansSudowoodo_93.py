from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="abce8386-f187-5935-91ba-c1993548c5f5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansSudowoodo.Name",
    display_name="Ethan's Sudowoodo",
    searchable_by=["Ethan's Sudowoodo", "Basic", "EthansSudowoodo"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=185,
    abilities=[
        Attack(
            title="Impound",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Try to Imitate",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)