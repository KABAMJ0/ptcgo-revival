from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import takes_less_passive
from ptcgo.game.card_effects.pokemon import energy_provides_type

def _my_pokemon_with_metal(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(child, PokemonTypes.METAL.value)
               for child in target.children)


gear_coating = takes_less_passive(20, protects=_my_pokemon_with_metal,
                                  stack_key="gear_coating")


card = PokemonCardDef(
    guid="e347b477-28ce-5a0a-9e10-6ed90c2e8117",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2", "Klinklang"],
    subtypes=["Stage 2"],
    collector_number=141,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Ability(
            title="Gear Coating",
            game_text="All of your Pok\u00e9mon that have any Metal Energy attached take 20 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance).",
            passive=gear_coating,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)