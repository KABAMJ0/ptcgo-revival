from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.session.effects import is_item_card


card = PokemonCardDef(
    guid="7a5cde1f-8344-5b3f-9fc3-b5f84d56df21",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    display_name="Tinkatink",
    searchable_by=["Tinkatink", "Basic", "Tinkatink"],
    subtypes=["Basic"],
    collector_number=216,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=957,
    abilities=[
        Attack(
            title="Scrap Pickup",
            game_text="Put an Item card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(is_item_card, count=1, minimum=1, reveal=False, to='hand'),
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)