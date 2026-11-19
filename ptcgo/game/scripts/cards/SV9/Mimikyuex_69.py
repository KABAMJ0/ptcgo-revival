from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from ptcgo.game.session.effects import is_special_energy

async def astral_barrage(ctx):
    """Choose 2 of your opponent's Pokemon and put 5 damage counters on each."""
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    chosen = await ctx.choose_cards(
        candidates, 2, prompt="Choose 2 of your opponent's Pokémon"
    )
    for target in chosen:
        await ctx.deal_damage(50, target=target, as_counters=True)

card = PokemonCardDef(
    guid="42cda9b0-a3cf-51cf-9bc5-6535cd0fc821",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyuex.Name",
    display_name="Mimikyu ex",
    searchable_by=["Mimikyu ex", "Basic", "ex", "Mimikyuex"],
    subtypes=["Basic", "ex"],
    collector_number=69,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=778,
    abilities=[
        Attack(
            title="Mischievous Hands",
            game_text="Choose 2 of your opponent's Pok\u00e9mon and put 3 damage counters on each of them.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=astral_barrage,
        ),
        Attack(
            title="Ghostly Trip",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)