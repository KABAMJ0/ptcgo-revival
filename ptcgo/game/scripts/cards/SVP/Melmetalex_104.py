from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import basic_energy_of

card = PokemonCardDef(
    guid="b04e985e-2120-5bd4-9d0a-fbca46842cda",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetalex.Name",
    display_name="Melmetal ex",
    searchable_by=["Melmetal ex", "Stage 1", "ex", "Melmetalex"],
    subtypes=["Stage 1", "ex"],
    collector_number=104,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=809,
    abilities=[
        Attack(
            title="Metal-bolize",
            game_text="Search your deck for up to 2 Basic Metal Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=search_attach_energy(basic_energy_of("metal"), count=2, to_self=True),
        ),
        Attack(
            title="Full Metal Knuckle",
            game_text="This attack does 30 more damage for each Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.METAL), per=30, base=90),
        ),
    ],
)