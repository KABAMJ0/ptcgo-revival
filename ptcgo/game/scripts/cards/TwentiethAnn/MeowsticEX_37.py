from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

from ptcgo.game.data_utils import Activations
from ptcgo.game.attributes import AttrID


async def shadow_ear(ctx):
    if not await ctx.ask_yes_no(
            "Move 1 damage counter from 1 of your Pokemon to 1 of your opponent's?"):
        return
    sources = [p for p in ctx.my_pokemon_in_play()
               if ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0) > 0]
    if not sources:
        return
    source = await ctx.choose_pokemon(sources, "Choose 1 of your damaged Pokemon")
    if source is None:
        return
    await ctx.move_damage_counters(
        source, ctx.opponent_pokemon_in_play(), max_count=1,
        prompt="Place the moved damage counter on 1 of your opponent's Pokemon")

card = PokemonCardDef(
    guid="74e60f4b-6ca9-5826-85e6-f254bdd5368a",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MeowsticEX.Name",
    display_name="Meowstic-EX",
    searchable_by=["Meowstic-EX", "Basic", "EX", "MeowsticEX"],
    subtypes=["Basic", "EX"],
    collector_number=37,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=678,
    abilities=[
        Ability(
            title="Shadow Ear",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may move 1 damage counter from 1 of your Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=shadow_ear,
        ),
        Attack(
            title="Mind Shock",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)