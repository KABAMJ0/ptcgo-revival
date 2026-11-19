from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="f5e0f5c7-ad75-5227-87dc-2dda0abed728",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Attack(
            title="Humming Charge",
            game_text="Search your deck for up to 2 Basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=search_attach_energy(predicate=is_basic_energy_card, count=2, to_self=True),
        ),
        Attack(
            title="Cotton Wings",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=100,
            effect=flip_protection(prevent=True),
        ),
    ],
)