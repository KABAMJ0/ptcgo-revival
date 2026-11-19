from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import previous_evolution_grant_passive


card = PokemonCardDef(
    guid="79c98781-0d51-5f68-a3d9-e7e89fca14b5",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name",
    display_name="Relicanth",
    searchable_by=["Relicanth", "Basic", "Relicanth"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=369,
    abilities=[
        Ability(
            title="Memory Dive",
            game_text="Each of your evolved Pok\u00e9mon can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)",
            passive=previous_evolution_grant_passive(),
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)