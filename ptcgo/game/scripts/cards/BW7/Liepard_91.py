from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import (PokemonCardDef, Attack, Ability, def_for,
                                    unimplemented)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def _assist(ctx):
    """Flip: on heads, use one of your Benched Pokemon's attacks as this one.

    The Active (this Pokemon) is the user; the Benched Pokemon is the printed
    `source`, which is what ctx.use_attack separates."""
    results = await ctx.flip_coins(1, "Assist")
    if not (results and results[0]):
        return
    candidates = []
    for pokemon in ctx.my_bench():
        definition = def_for(pokemon.archetype_id)
        for attack in getattr(definition, "abilities", []) or []:
            if isinstance(attack, Attack):
                candidates.append((pokemon, attack))
    if not candidates:
        return
    picked = candidates[0] if len(candidates) == 1 else \
        await ctx.choose_attack_to_copy(candidates, "Choose an attack to use")
    if picked is None:
        return
    source, attack = picked
    await ctx.use_attack(attack, source=source)


card = PokemonCardDef(
    guid="706f6a5e-33c1-5912-85d8-044837a7cf1e",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard", "Stage 1", "Liepard"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Tail Trickery",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Assist",
            game_text="Flip a coin. If heads, choose 1 of your Benched Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            effect=_assist,
        ),
    ],
)