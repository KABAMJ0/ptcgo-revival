from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _dual_brains(ctx):
    """One more Supporter this turn."""
    ctx.allow_extra_supporter(1)


card = PokemonCardDef(
    guid="c3a92e1d-6901-515b-b5a1-2fdf3e761303",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Team Plasma", "Magnezone"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=46,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Dual Brains",
            game_text="During your turn, you may play 2 Supporter cards.",
            activation=Activations.ONCE_PER_TURN,
            effect=_dual_brains,
        ),
        Attack(
            title="Gyro Ball",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. Then, your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)