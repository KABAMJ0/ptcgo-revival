from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import search_attach_energy


async def stoke(ctx):
    """Search the deck for a Fire Energy and attach it to Ho-Oh."""
    await search_attach_energy(lambda card: energy_provides_type(card, PokemonTypes.FIRE.value),
                               count=1, to_self=True, shuffle=True,
                               prompt="Choose a Fire Energy to attach")(ctx)

card = PokemonCardDef(
    guid="25ff4c77-b907-5811-912a-4281811ea431",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hooh.Name",
    display_name="Ho-oh",
    searchable_by=["Ho-oh", "Basic", "Hooh"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Attack(
            title="Stoke",
            game_text="You may search your deck for a Fire Energy card and attach it to Ho-Oh. Shuffle your deck afterward.",
            cost={PokemonTypes.FIRE: 1},
            effect=stoke,
        ),
        Attack(
            title="Sacred Fire",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.FIRE: 3},
            effect=unimplemented,
        ),
        Attack(
            title="Dive Bomb",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 5},
            damage=90,
            effect=flip_or_nothing(),
        ),
    ],
)