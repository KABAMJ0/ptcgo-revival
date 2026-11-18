from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2dca0b05-2a70-55bd-973f-39eab8ffdfab",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiram.Name",
    display_name="Reshiram",
    searchable_by=["Reshiram", "Basic", "Reshiram"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="BW1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Outrage",
            game_text="Does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Blue Flare",
            game_text="Discard 2 Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.FIRE),
        ),
    ],
)