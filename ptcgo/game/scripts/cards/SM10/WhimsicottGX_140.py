from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
from ptcgo.game.card_effects.passives_common import flip_prevent_damage_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0de5f411-3e11-5513-b6c0-06516b5c8831",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhimsicottGX.Name",
    display_name="Whimsicott-GX",
    searchable_by=["Whimsicott-GX", "Stage 1", "GX", "WhimsicottGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=140,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=190,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Ability(
            title="Fluffy Cotton",
            game_text="If any damage is done to this Pok\u00e9mon by attacks, flip a coin. If heads, prevent that damage.",
            passive=flip_prevent_damage_passive("Fluffy Cotton"),
        ),
        Attack(
            title="Energy Blow",
            game_text="This attack does 30 more damage times the amount of Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("self"), per=30, base=10),
        ),
        Attack(
            title="Toy Box-GX",
            game_text="Search your deck for up to 5 cards and put them into your hand. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1},
            effect=search_to_hand(count=5, minimum=0),
        ),
    ],
)
