from ptcgo.game.card_effects.attacks_common import count_retreat_cost, damage_per
from ptcgo.game.card_effects.support_common import gust_attack, switch_self_attack
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented


async def _slippery_soles(ctx):
    """Switch my Active with a Benched one; if I did, the opponent switches
    theirs too."""
    switched = await switch_self_attack(optional=True)(ctx)
    if switched is None:
        return
    await gust_attack(damage_before=0, opponent_chooses=True)(ctx)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9d8bdbc4-454c-52f5-ac05-13fdd5fe6002",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2", "Vanilluxe"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="BW4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Ability(
            title="Slippery Soles",
            game_text="Once during your turn (before your attack), you may switch your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. If you do, your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=_slippery_soles,
        ),
        Attack(
            title="Crushing Ice",
            game_text="Does 10 more damage for each Colorless Energy in the Defending Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_retreat_cost("defender"), 10, base=60),
        ),
    ],
)