from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import discard_from_hand_then
from ptcgo.game.attributes import AttrID

def _metal_pokemon(card):
    from ptcgo.game.attributes import CardType
    if card.get_attribute(AttrID.CARD_TYPE) != CardType.POKEMON.value:
        return False
    return PokemonTypes.METAL.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


async def _heal_100(ctx):
    await ctx.heal(100, target=ctx.source)


# "You may discard a Metal Pokemon from your hand. If you do, heal 100."
metal_eater = discard_from_hand_then(_metal_pokemon, 1, _heal_100,
                                     prompt="Discard a Metal Pokemon from your hand")


card = PokemonCardDef(
    guid="1905b3fa-50aa-5e63-bd80-e75b320a91d1",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetal.Name",
    display_name="Melmetal",
    searchable_by=["Melmetal", "Stage 1", "Melmetal"],
    subtypes=["Stage 1"],
    collector_number=181,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Ability(
            title="Metal Eater",
            game_text="Once during your turn (before your attack), you may discard a Metal Pok\u00e9mon from your hand. If you do, heal 100 damage from this Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=metal_eater,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)