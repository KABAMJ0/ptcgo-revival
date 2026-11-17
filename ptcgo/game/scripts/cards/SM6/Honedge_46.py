from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="93dc3e9c-f951-5d11-8ecf-e6777201c323",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    display_name="Honedge",
    searchable_by=["Honedge", "Basic", "Honedge"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=679,
    abilities=[
        Ability(
            title="Final Hour",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is Knocked Out by damage from an opponent's attack, put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=50,
        ),
    ],
)