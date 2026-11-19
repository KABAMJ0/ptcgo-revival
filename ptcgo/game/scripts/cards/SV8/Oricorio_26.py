from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="6f3b3b73-e8ed-512b-93dc-a7baa554536e",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Oricorio"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=741,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Attach up to 2 Basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            effect=attach_from_discard(predicate=is_basic_energy_card, count=2, minimum=0, target=lambda p: not is_in_active_spot(p), prompt='Choose up to 2 basic Energy cards to attach'),
        ),
        Attack(
            title="Fireworks",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)