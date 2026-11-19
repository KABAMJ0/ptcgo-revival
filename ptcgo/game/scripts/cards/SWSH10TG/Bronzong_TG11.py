from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type


def _metal_transfer_condition(board, player_id, pokemon):
    pkmn = board.pokemon_in_play(player_id)
    if len(pkmn) < 2:
        return False
    return any(
        energy_provides_type(e, PokemonTypes.METAL)
        for p in pkmn for e in board.attached_energies(p)
    )


async def metal_transfer(ctx):
    pool = [
        (e, p) for p in ctx.my_pokemon_in_play()
        for e in ctx.attached_energies(p)
        if energy_provides_type(e, PokemonTypes.METAL)
    ]
    if not pool:
        return
    picked = await ctx.choose_cards(
        [e for e, _ in pool], 1, prompt="Choose a Metal Energy to move"
    )
    if not picked:
        return
    energy = picked[0]
    holder = next(p for e, p in pool if e is energy)
    targets = [p for p in ctx.my_pokemon_in_play() if p is not holder]
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose a Pokémon to move the Energy to")
    if target is not None:
        await ctx.move_energy(energy, target)

card = PokemonCardDef(
    guid="1880a3ee-d641-5c18-b47b-d01fc6fb7518",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SWSH10TG",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=437,
    abilities=[
        Ability(
            title="Metal Transfer",
            game_text="As often as you like during your turn, you may move a Metal Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=metal_transfer,
            condition=_metal_transfer_condition,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)