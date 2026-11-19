from ptcgo.game.card_effects.attacks_common import move_counters_attack
from ptcgo.game.card_effects.passives_common import effective_max_hp
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def _curse_breath(ctx):
    board = ctx.session.board_state
    for player_id in (ctx.player_id, ctx.opponent_id):
        for pokemon in board.pokemon_in_play(player_id):
            if pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon):
                await ctx.deal_damage(10, target=pokemon, as_counters=True)

card = PokemonCardDef(
    guid="148f8b56-db87-5d6d-b1dd-1c729cf0b8b7",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=442,
    abilities=[
        Ability(
            title="Curse Breath",
            game_text="Once during your turn, when you put Spiritomb from your hand onto your Bench, you may put 1 damage counter on all Pok\u00e9mon that already have any damage counters on them (both yours and your opponent's). You can't use more than 1 Curse Breath Pok\u00e9-Power each turn.",
            trigger=Triggers.ON_PLAY,
            effect=_curse_breath,
        ),
        Attack(
            title="Transfer Pain",
            game_text="Move 1 damage counter from 1 of your Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=move_counters_attack(1, dest="choice"),
        ),
    ],
)