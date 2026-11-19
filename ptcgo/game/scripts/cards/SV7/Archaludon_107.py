from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.card_effects.passives_common import retreat_free_when
from ptcgo.game.card_effects.pokemon import energy_provides_type

def _my_pokemon_with_metal_energy(pokemon, carrier):
    if pokemon.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(child, PokemonTypes.METAL.value)
               for child in pokemon.children)


card = PokemonCardDef(
    guid="84506355-b074-55af-9f3d-48a4325b1363",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archaludon.Name",
    display_name="Archaludon",
    searchable_by=["Archaludon", "Stage 1", "Archaludon"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    family_id=884,
    abilities=[
        Ability(
            title="Metal Bridge",
            game_text="All of your Pok\u00e9mon that have Metal Energy attached have no Retreat Cost.",
            passive=retreat_free_when(_my_pokemon_with_metal_energy),
        ),
        Attack(
            title="Iron Blaster",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=lock_self_attack(),
        ),
    ],
)