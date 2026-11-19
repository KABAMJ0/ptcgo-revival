from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import attach_from_discard

PSYCHIC = PokemonTypes.PSYCHIC.value


def _is_psychic_energy(card):
    return energy_provides_type(card, PSYCHIC)


async def _stardust_song(ctx):
    results = await ctx.flip_coins(3, "Stardust Song")
    heads = sum(1 for result in results if result)
    if heads:
        await attach_from_discard(_is_psychic_energy, count=heads, target="self",
                                  minimum=0)(ctx)


card = PokemonCardDef(
    guid="c35221d3-5cfa-5437-bae9-4b20d68e54a9",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=385,
    abilities=[
        Ability(
            title="Stardust Song",
            game_text="Once during your turn, when you put Jirachi from your hand onto your Bench, you may flip 3 coins. For each heads, search your discard pile for a Psychic Energy card and attach it to Jirachi.",
            trigger=Triggers.ON_PLAY,
            effect=unimplemented,
        ),
        Attack(
            title="Time Hollow",
            game_text="Choose a number of your opponent's Stage 1 or Stage 2 Evolved Pok\u00e9mon up to the amount of Energy attached to Jirachi. Remove the highest Stage Evolution card from each of those Pok\u00e9mon and put those cards back into your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)