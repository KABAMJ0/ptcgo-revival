from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="99cd467f-1468-5734-814d-68fe5bcd57d2",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChienPao.Name",
    display_name="Chien-Pao",
    searchable_by=["Chien-Pao", "Basic", "ChienPao"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=1002,
    abilities=[
        Attack(
            title="Snow Bringer",
            game_text="Attach up to 2 Basic Water Energy cards from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=attach_from_discard(basic_energy_of("water"), count=2, minimum=0, target="choice"),
        ),
        Attack(
            title="Wrathful Blade",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)