from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0c5cc0b0-b888-5c1f-954e-bf9ddb0aefba",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name",
    display_name="Deerling",
    searchable_by=["Deerling", "Basic", "Deerling"],
    subtypes=["Basic"],
    collector_number=165,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=585,
    abilities=[
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Leaf Litter Tackle",
            game_text="Discard a Grass Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.GRASS),
        ),
    ],
)