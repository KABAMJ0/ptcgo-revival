from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
from ptcgo.game.card_effects.pokemon import is_lightning_energy


async def electrify(ctx):
    """Search up to 2 Lightning Energy and attach them to your Benched
    Pokémon in any way you like."""
    bench_ids = {p.entity_id for p in ctx.my_bench()}
    await search_attach_energy(
        is_lightning_energy, count=2,
        target_pred=lambda p: p.entity_id in bench_ids,
    )(ctx)


card = PokemonCardDef(
    guid="5bf8fae9-5598-51dc-bb62-91b23f6dcb7a",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BoltundV.Name",
    display_name="Boltund V",
    searchable_by=["Boltund V", "Basic", "V", "BoltundV"],
    subtypes=["Basic", "V"],
    collector_number=13,
    set_code="SWSH9TG",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=836,
    abilities=[
        Attack(
            title="Electrify",
            game_text="Search your deck for up to 2 Lightning Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=electrify,
        ),
        Attack(
            title="Bolt Storm",
            game_text="This attack does 30 more damage for each Lightning Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(
                count_energy("mine", energy_type=PokemonTypes.LIGHTNING), 30, base=10
            ),
        ),
    ],
)