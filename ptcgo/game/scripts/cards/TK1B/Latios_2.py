from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def gather_energy(ctx):
    await ctx.deal_damage()
    flips = await ctx.flip_coins(1, "Gather Energy")
    if flips and flips[0]:
        picks = await ctx.search_deck(
            is_basic_energy_card, count=1, minimum=0,
            prompt="Choose a basic Energy card to attach.",
        )
        if picks:
            target = await ctx.choose_pokemon(
                ctx.my_pokemon_in_play(),
                "Choose a Pok\u00e9mon to attach the Energy to",
            )
            if target is not None:
                await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="a056759f-348b-5ee7-b5ab-3fc73b20f249",
    key="TK1B",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios",
    searchable_by=["Latios", "Basic", "Latios"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="TK1B",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=381,
    abilities=[
        Attack(
            title="Gather Energy",
            game_text="Flip a coin. If heads, search your deck for a basic Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=gather_energy,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)