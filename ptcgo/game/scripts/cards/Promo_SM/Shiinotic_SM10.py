from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CardType, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.support_common import search_to_hand


def _is_grass_pokemon(card) -> bool:
    return (card.get_attribute(AttrID.CARD_TYPE) == CardType.POKEMON.value
            and PokemonTypes.GRASS.value
            in (card.get_attribute(AttrID.POKEMON_TYPES) or []))

card = PokemonCardDef(
    guid="4a9896c8-761c-53bf-b93a-a150603339c0",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiinotic.Name",
    display_name="Shiinotic",
    searchable_by=["Shiinotic", "Stage 1", "Shiinotic"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    family_id=756,
    abilities=[
        Ability(
            title="Illuminate",
            game_text="Once during your turn (before your attack), you may search your deck for a Grass Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=search_to_hand(_is_grass_pokemon, count=1, reveal=True),
        ),
        Attack(
            title="Flickering Spores",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)