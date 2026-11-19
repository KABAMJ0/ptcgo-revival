from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, is_basic_energy_card

card = PokemonCardDef(
    guid="7cdfeb87-53a4-526b-8b17-87f653ff1b3c",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYu.Name",
    display_name="Chi-Yu",
    searchable_by=["Chi-Yu", "Basic", "ChiYu"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1004,
    abilities=[
        Attack(
            title="Flare Bringer",
            game_text="Attach up to 2 Basic Fire Energy cards from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            effect=attach_from_discard(basic_energy_of("fire"), count=2, minimum=0, target="choice"),
        ),
        Attack(
            title="Megafire of Envy",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)