from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fe326323-ac98-5c09-a6e0-c4bf4951f791",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigusex.Name",
    display_name="Cofagrigus ex",
    searchable_by=["Cofagrigus ex", "Stage 1", "ex", "Cofagrigusex"],
    subtypes=["Stage 1", "ex"],
    collector_number=76,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Ability(
            title="Gold Coffin",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Hollow Hands",
            game_text="Put 5 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=110,
            effect=unimplemented,
        ),
    ],
)