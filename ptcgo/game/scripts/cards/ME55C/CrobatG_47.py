from ptcgo.game.data_utils import Triggers
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented


async def _flash_bite(ctx):
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to put 1 damage counter on")
    if target is not None:
        await ctx.place_damage_counters(1, [target])

from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="84ca21f2-886b-567c-9961-99d222f1c45c",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatG.Name",
    display_name="Crobat G",
    searchable_by=["Crobat G", "Basic", "CrobatG"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="ME55C",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=169,
    abilities=[
        Ability(
            title="Flash Bite",
            game_text="Once during your turn, when you put Crobat G from your hand onto your Bench, you may put 1 damage counter on 1 of your opponent's Pok\u00e9mon.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=_flash_bite,
        ),
        Attack(
            title="Toxic Fang",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on the Defending Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED, counters=2),
        ),
    ],
)