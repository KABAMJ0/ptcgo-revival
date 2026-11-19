from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers

async def biting_whirlpool(ctx):
    """Whenever your opponent attaches an Energy card from their hand to 1 of
    their Pokémon, put 2 damage counters on that Pokémon."""
    if ctx.attaching_player_id == ctx.player_id:
        return
    receiver = ctx.energy_receiver
    if receiver is None:
        return
    await ctx.deal_damage(20, target=receiver, apply_modifiers=False, as_counters=True)

card = PokemonCardDef(
    guid="ef29d71d-1abb-50c7-b584-5686a0431c19",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arctozolt.Name",
    display_name="Arctozolt",
    searchable_by=["Arctozolt", "Stage 1", "Arctozolt"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RareFossil.Name",
    family_id=881,
    abilities=[
        Ability(
            title="Biting Whirlpool",
            game_text="Whenever your opponent attaches an Energy card from their hand to 1 of their Pok\u00e9mon, put 2 damage counters on that Pok\u00e9mon.",
            effect=biting_whirlpool,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)