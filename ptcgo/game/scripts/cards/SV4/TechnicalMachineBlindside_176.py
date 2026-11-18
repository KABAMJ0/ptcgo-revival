from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities, AttrID, PokemonTypes
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.session.passives import effective_max_hp

async def _blindside_attack(ctx):
    def _damaged(pokemon):
        return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(ctx.board, pokemon)

    await snipe_attack(100, pool=_damaged, count=1)(ctx)


card = PokemonToolCardDef(
    guid="1a7325dd-c11d-5260-a965-6aeb1fc35b84",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineBlindside.Name",
    display_name="Technical Machine: Blindside",
    searchable_by=["Technical Machine: Blindside", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=176,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Blindside",
            game_text="This attack does 100 damage to 1 of your opponent's "
                      "Pokémon that has any damage counters on it. (Don't apply "
                      "Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=_blindside_attack,
        ),
        Ability(
            title="Technical Machine: Blindside",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
