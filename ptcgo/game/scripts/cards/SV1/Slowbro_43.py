from ptcgo.game.card_effects.passives_common import effective_max_hp
from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def _strange_behavior(ctx):
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if p is not ctx.source
                  and p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not candidates:
        return
    source = await ctx.choose_pokemon(
        candidates, "Choose a Pok\u00e9mon to move a damage counter from")
    if source is None:
        return
    await ctx.move_damage_counters(source, ctx.source, max_count=1,
                                   prompt="Move a damage counter to this Pok\u00e9mon")


def _strange_behavior_offered(board, player_id, pokemon):
    return any(p is not pokemon and p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
               for p in board.pokemon_in_play(player_id))


card = PokemonCardDef(
    guid="cdff2f0b-5aef-546f-8735-eb09c3b0058f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Strange Behavior",
            game_text="As often as you like during your turn, you may move 1 damage counter from 1 of your other Pok\u00e9mon to this Pok\u00e9mon.",
            effect=_strange_behavior,
            activation=Activations.UNLIMITED,
            condition=_strange_behavior_offered,
        ),
        Attack(
            title="Bubble Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=heal_attack(30),
        ),
    ],
)
