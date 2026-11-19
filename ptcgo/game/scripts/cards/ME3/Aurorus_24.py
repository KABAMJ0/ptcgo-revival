from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import takes_less_passive
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.models.board import BoardState


def _water_energy_team(target, carrier) -> bool:
    """Your Pokemon with any Water Energy attached (Tundra Wall)."""
    if target.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(energy, PokemonTypes.WATER.value)
               for energy in BoardState.attached_energies(target))


card = PokemonCardDef(
    guid="d41c7e50-9891-5283-bc56-44df2d807308",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aurorus.Name",
    display_name="Aurorus",
    searchable_by=["Aurorus", "Stage 2", "Aurorus"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Amaura.Name",
    family_id=698,
    abilities=[
        Ability(
            title="Tundra Wall",
            game_text="All of your Pok\u00e9mon that have any Water Energy attached take 50 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance). The effect of Tundra Wall doesn't stack.",
            passive=takes_less_passive(50, protects=_water_energy_team,
                                      stack_key="Tundra Wall"),
        ),
        Attack(
            title="Freezing Chill",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)