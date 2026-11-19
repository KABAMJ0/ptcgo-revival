from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive


class SpectralBreachPassive(Passive):
    """All Special Energy (both players') provide only Colorless Energy."""

    def suppresses_special_energy(self, energy, carrier) -> bool:
        return True


card = PokemonCardDef(
    guid="f4c6726d-ba42-558d-a9e0-eae085d7e6f9",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="SWSH9TG",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Spectral Breach",
            game_text="All Special Energy attached to Pokémon (both yours and your opponent's) provide Colorless Energy and have no other effect.",
            passive=SpectralBreachPassive(),
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
