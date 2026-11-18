from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3563d2b6-ed4d-5826-843b-0fb088948841",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasFeebas.Name",
    display_name="Cynthia's Feebas",
    searchable_by=["Cynthia's Feebas", "Basic", "CynthiasFeebas"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=349,
    abilities=[
        Attack(
            title="Undulate",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)