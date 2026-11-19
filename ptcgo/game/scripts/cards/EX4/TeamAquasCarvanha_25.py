from ptcgo.game.card_effects.passives_common import retreat_free_when
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _has_darkness(pokemon, carrier):
    if carrier_pokemon(carrier) is not pokemon:
        return False
    return any(energy_provides_type(child, PokemonTypes.DARKNESS.value)
               for child in pokemon.children)

card = PokemonCardDef(
    guid="9e850cbe-76ae-5685-b5da-83c1d87e7ba9",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCarvanha.Name",
    display_name="Team Aqua's Carvanha",
    searchable_by=["Team Aqua's Carvanha", "Basic", "TeamAquasCarvanha"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=318,
    abilities=[
        Ability(
            title="Dark Lift",
            game_text="If Team Aqua's Carvanha has any Darkness Energy attached to it, the Retreat Cost for Team Aqua's Carvanha is 0.",
            passive=retreat_free_when(_has_darkness),
        ),
        Attack(
            title="Slow-Acting Poison",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
    ],
)