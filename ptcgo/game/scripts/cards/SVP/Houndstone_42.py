from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.session.effects import is_item_card


card = PokemonCardDef(
    guid="b5ff2819-b9a4-5f5c-b4cc-9a9d1a2b51bc",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndstone.Name",
    display_name="Houndstone",
    searchable_by=["Houndstone", "Stage 1", "Houndstone"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    family_id=971,
    abilities=[
        Attack(
            title="Delve",
            game_text="Put up to 2 Item cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=recover_from_discard(is_item_card, count=2, to='hand'),
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)