from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card, pokemon_named
from ptcgo.game.card_effects.attacks_common import damage_per, count_in_play

card = PokemonCardDef(
    guid="759db410-b0c5-55ea-b2c8-b619c162a9f1",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMarowak.Name",
    display_name="Alolan Marowak",
    searchable_by=["Alolan Marowak", "Stage 1", "AlolanMarowak"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=105,
    abilities=[
        Attack(
            title="Limbo Limbo",
            game_text="Search your deck for up to 2 basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={},
            effect=search_attach_energy(is_basic_energy_card, count=2),
        ),
        Attack(
            title="Alolan Club",
            game_text="This attack does 20 damage for each of your Pok\u00e9mon in play that has Alolan in its name.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", pokemon_named("Alolan")), 20),
        ),
    ],
)