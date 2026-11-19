from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f8adbbbe-efd6-5f14-aa09-652be8bbb7aa",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=115,
    set_code="BW1",
    rarity=Rarities.RareSecret,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Energize",
            game_text="Attach a Lightning Energy from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=attach_from_discard(basic_energy_of("lightning"), count=1,
                                       target="self"),
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)