from ptcgo.game.card_effects.attacks_common import flip_damage_condition
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_energy_card


async def dance_of_flames(ctx):
    """Attach one Fire Energy from your discard pile to your Pokemon for each
    Energy attached to the opponent's Pokemon, placed as you like."""
    count = sum(len(ctx.attached_energies(p))
                for p in ctx.opponent_pokemon_in_play())
    fire = [card for card in ctx.discard_pile()
            if is_energy_card(card)
            and energy_provides_type(card, PokemonTypes.FIRE.value)]
    for _ in range(min(count, len(fire))):
        picks = await ctx.choose_cards(
            fire, 1, prompt="Choose a Fire Energy card to attach")
        if not picks:
            return
        card = picks[0]
        fire.remove(card)
        targets = ctx.my_pokemon_in_play()
        if not targets:
            return
        target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
            targets, "Choose a Pokémon to attach the Energy to")
        if target is None:
            return
        await ctx.attach_energy(card, target)


card = PokemonCardDef(
    guid="94a6977f-b587-570d-9014-692268f1958a",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMarowak.Name",
    display_name="Alolan Marowak",
    searchable_by=["Alolan Marowak", "Stage 1", "AlolanMarowak"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Dance of Flames",
            game_text="For each Energy attached to your opponent's Pok\u00e9mon, attach a Fire Energy card from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={},
            effect=dance_of_flames,
        ),
        Attack(
            title="Burning Bonemerang",
            game_text="Flip 2 coins. This attack does 70 damage for each heads. If either of them is heads, your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=flip_damage_condition(2, per_heads=70, min_heads=1, condition=SpecialConditions.BURNED),
        ),
    ],
)