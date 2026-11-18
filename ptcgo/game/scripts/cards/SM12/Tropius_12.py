from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack, search_attach_energy
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_energy_card


def _is_grass_energy(card) -> bool:
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.GRASS.value)

card = PokemonCardDef(
    guid="03265989-fea7-5e88-8357-1f0d19f47cb3",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic", "Tropius"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Attack(
            title="Synthesis",
            game_text="Search your deck for a Grass Energy card and attach it to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(_is_grass_energy, count=1,
                                       distribute=False),
        ),
        Attack(
            title="Leaf Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=heal_attack(30, target="self"),
        ),
    ],
)