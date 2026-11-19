from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.content.definitions import Activations
from ptcgo.game.session.passives import effective_max_hp
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

def _heal_dance_candidates(ctx):
    return [pokemon for pokemon in ctx.my_pokemon_in_play()
            if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)]


def heal_dance_condition(board, player_id, pokemon):
    if pokemon is None or pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    return any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
               for p in board.pokemon_in_play(player_id))


async def heal_dance(ctx):
    candidates = _heal_dance_candidates(ctx)
    if not candidates:
        return 0
    target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to remove 2 damage counters from")
    if target is None:
        return 0
    return await ctx.heal(20, target)

card = PokemonCardDef(
    guid="12e02733-16aa-5c5f-9fee-8d08be4740e3",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Heal Dance",
            game_text="Once during your turn (before your attack), you may remove 2 damage counter from 1 of your Pok\u00e9mon. You can't use more than 1 Heal Dance Pok\u00e9-Power each turn. This power can't be used if Gardevoir is affected by a Special Condition.",
            effect=heal_dance,
            activation=Activations.ONCE_PER_TURN,
            condition=heal_dance_condition,
            shared_once_per_turn="Heal Dance",
        ),
        Attack(
            title="Psypunch",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Mind Shock",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)